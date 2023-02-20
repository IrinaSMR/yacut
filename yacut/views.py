from flask import flash, redirect, render_template

from . import app
from .forms import URL_mapForm, ORIGINAL_LINK_LABEL
from .models import URLMap

ALREADY_EXISTS = 'Имя {custom_id} уже занято!'
FORM_ERROR = f'"{ORIGINAL_LINK_LABEL}" является обязательным полем!'


@app.route('/<string:id>')
def get_original_url(id):
    return redirect(
        URLMap.query.filter_by(short=id).first_or_404().original)


@app.route('/', methods=['GET', 'POST'])
def yacut_view():
    form = URL_mapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = 'custom_id'
    try:
        custom_id = URLMap.check_or_generate_short_url(form[custom_id].data)
    except ValueError as error:
        flash(str(error))
        return render_template('index.html', form=form)
    if URLMap.get(short=custom_id):
        flash(ALREADY_EXISTS.format(custom_id=custom_id))
        return render_template('index.html', form=form)
    return render_template(
        'index.html',
        form=form,
        short_url=URLMap.add(
            original=form.original_link.data,
            short=custom_id
        ).get_short_url()
    )

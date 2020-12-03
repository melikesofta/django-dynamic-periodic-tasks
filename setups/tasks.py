from celery import shared_task

from .models import Setup


@shared_task(name="computation_heavy_task")
def computation_heavy_task(setup_id):
    setup = Setup.objects.get(id=setup_id)

    # Do heavy computation with variables in setup model here.

    print('''Running task for setup {setup_title}.'''.format(
        setup_title=setup.title))

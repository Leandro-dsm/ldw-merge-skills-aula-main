from flask_frozen import Freezer
from app import  create_app

app = create_app()
freezer = Freezer(app)


@freezer.register_generator
def curso_detalhe():
    for curso in app.config.get('CURSOS', []):
        yield {'curso_id': curso['id']}

if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    freezer.freeze()
    print("Site estatico gerado em /build")
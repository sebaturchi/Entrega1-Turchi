README

.Es un repositorio para poder crear una pagina web en donde se crea una base de datos con contenido de distintas clases, como en este caso son los "Profesores", "Estudiantes", y "Cursos".

.En este caso es la segunda version para la reentrega del "Proyecto medio" del curso Python de Coderhouse.



.Se trata de distintos modulos de Python entrelazados, cada uno con una funcionalidad distinta:

-views.py: Para trabajar la logica de cada url.

-urls.py: Para organizar las distintas subpaginas que contiene la web. Se le aplica cual va a ser la direccion de cada apartado, y a cada una se le otorgara una vista extraida del modulo "views.py".

-models.py: Donde se desarrollan las clases que van a tomar los datos que se les importe, los cuales se veran alojados en la base de datos.

-forms.py: Se establecen los formularios para otorgarle la informacion a cada modelo. Tambien util para no sobrecargar de logica a los templates.

-admin.py: El organizador del proyecto que computa cuales van a ser los modelos a utilizar.


El orden de funcionamiento es a partir de lo que el usuario pide hacer en determinada url relacionarlo con la logica inscripta en el modulo "views" el cual va a estar apoyado por los modelos y los formularios. Una vez que haya procesado la peticion del usuario entonces va a mostrar una respuesta a traves de un template en formato html, el cual contiene graficos estaticos creados mediante javascript y css.





Repositorio creado por Sebastian Turchi para la plataforma educativa Coderhouse, curso de Python.
**Zodiacally** es un proyecto de software diseñado para explorar la identidad astronómica y cultural a través de la programación. El objetivo es que, con una sola fecha de nacimiento, el usuario obtenga su perfil en múltiples sistemas zodiacales.

## Características Técnicas
- **Modularidad:** Separación total entre la interfaz (`main.py`) y los motores de cálculo (`europeos.py`).
- **Validación Dinámica:** Uso de la librería `calendar` para validación de fechas reales y años bisiestos.
- **Lógica de Rangos:** Sistema de comparación de tuplas para determinar signos, incluso en periodos que cruzan el cambio de año.

## Planteamiento del sistema
### Modo Python CLI
Motor de cálculo para identidades zodiacales bajo múltiples sistemas culturales.
#### Sistemas Actuales (Modo Europeo)
- [x] **Europeo Tropical:** Zodiaco convencional (Aries, Tauro...).
- [x] **Europeo Sideral:** Basado en la posición astronómica real.
- [x] **Europeo Druídico:** Basado en la astrología lunar celta.
- [x] **Astrología Rúnica Nórdica:** Veinticuatro runas, antigua sabiduría vikinga.
- [x] **Astrología Védica (Jyotish):** El ojo de los Vedas, antigua astrología sidérea india.

#### En Desarrollo
- [ ] **Zodiaco Oriental (Chino):** Lógica basada en ciclos de 12 años y años nuevos lunares.
- [ ] **Calendario Celta de los Árboles:** Trece árboles sagrados, el año lunar druídico.

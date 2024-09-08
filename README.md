# Sistema de Gestión de Citas Médicas

Este proyecto es un sistema de gestión de citas médicas diseñado para permitir a los pacientes solicitar citas, a los médicos gestionar sus agendas y generar reportes detallados. El sistema incluye funciones para notificaciones, verificación de disponibilidad y cancelación de citas, y está basado en los requerimientos obtenidos del cliente.

## Funcionalidades Principales

- **Verificación de Disponibilidad**: El sistema verifica la disponibilidad de los médicos según su especialidad y la fecha de la cita.
- **Asignación de Médico Preferido**: Los pacientes pueden seleccionar un médico preferido para futuras citas.
- **Gestión de Agenda**: Los médicos tienen una agenda donde se almacenan las citas pendientes y realizadas.
- **Notificaciones**: Se envían notificaciones a los pacientes para recordar sus citas a través de llamadas, mensajes de texto o correo electrónico.
- **Cancelación y Reprogramación de Citas**: Los pacientes pueden cancelar y reprogramar citas según la disponibilidad de los médicos.
- **Generación de Reportes**: El sistema puede generar reportes de demanda, tendencias de citas, causas de cancelaciones, y ausentismo, los cuales pueden exportarse a Excel.

## Requisitos del Sistema

- Python 3.x
- Librerías adicionales no requeridas (el sistema está basado en funciones estándar de Python).

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/SSamuelP/Sistema-Consultas-medicas.git
    cd sistema-citas-medicas
    ```

2. Asegúrate de tener Python 3.x instalado. Puedes verificarlo con el siguiente comando:

    ```bash
    python --version
    ```

3. Asegurate de haber descargado los requerimientos.
    ```bash
    pip install requirements.txt
    ```

4. Ejecuta el archivo `main.py` desde la terminal o consola de tu sistema operativo para interactuar con el menú.

    ```bash
    python main.py
    ```

## Uso del Sistema

El sistema funciona a través de un menú interactivo en la consola que permite realizar diversas operaciones. A continuación, se detallan algunas de las acciones disponibles:

### Menú de Opciones:

1. **Agregar Paciente**: Permite registrar un nuevo paciente en el sistema.
2. **Agregar Médico**: Permite registrar un médico, junto con su especialidad.
3. **Solicitar Cita**: Un paciente puede solicitar una cita con un médico disponible.
4. **Cancelar Cita**: Los pacientes pueden cancelar una cita programada.
5. **Reprogramar Cita**: Permite cambiar la fecha de una cita existente.
6. **Mostrar Cupos Disponibles**: Verifica la disponibilidad de un médico en una especialidad específica.
7. **Generar Reporte de Demanda**: Muestra un reporte de la demanda de citas por especialidad.
8. **Generar Reporte de Tendencias**: Genera un reporte con las tendencias de citas a lo largo del tiempo.
9. **Generar Reporte de Cancelaciones**: Muestra un reporte con las causas de cancelación de citas.
10. **Generar Reporte de Ausentismo**: Crea un reporte del porcentaje de ausentismo de pacientes.
11. **Salir**: Cierra el sistema.

## Clases Principales

### 1. **Agenda**
   Maneja las citas pendientes y realizadas de un médico o paciente.

### 2. **Cita**
   Representa una cita médica, con atributos como paciente, médico, fecha, y motivo de cancelación.

### 3. **Paciente**
   Contiene la información del paciente y permite solicitar o cancelar citas.

### 4. **Médico**
   Contiene los detalles de un médico, incluida su especialidad y disponibilidad.

### 5. **Hospital**
   Es una clase singleton que almacena a los médicos y pacientes registrados en el sistema.

### 6. **Reporte**
   Clase base para generar diferentes tipos de reportes, con subclases específicas para demanda, tendencias, cancelaciones y ausentismo.

### 7. **Correo, Aplicacion, Celular**
   Clases utilizadas para enviar notificaciones a los pacientes.

## Ejecución del Menú

El menú interactivo permite ejecutar todas las funcionalidades del sistema. Para ejecutarlo, simplemente corre el archivo principal `main.py`, donde se podrán agregar pacientes, médicos, solicitar citas y cancelar citas.


## Futuras Mejoras

- Integración con plataformas de mensajería como WhatsApp o Slack para mejorar la comunicación con los pacientes.

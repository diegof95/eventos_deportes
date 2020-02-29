Feature: Crear evento
Yo como gerente quiero crear un evento deportivo para poder ofrecerlo al público.

  Background:
    Given Gerente "Diego"
    And Estoy logueado como "Diego"

  Scenario: Diego crea un evento de Tenis
    Given Diego selecciona Nuevo evento
    And Evento a crear es valido
    When Diego selecciona Crear evento
    Then Diego ve mensaje de Evento creado
    And Diego es redireccionado a Lista de eventos activos
    
    
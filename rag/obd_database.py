OBD_DATABASE = {

    "P0300": {
        "description": "Random or multiple cylinder misfire detected",
        "system": "Engine / Ignition / Fuel",
        "possible_causes": [
            "Ignition system problems",
            "Fuel delivery problems",
            "Air/fuel mixture problems",
            "Vacuum or intake leaks",
            "Engine mechanical problems"
        ]
    },

    "P0301": {
        "description": "Cylinder 1 misfire detected",
        "system": "Engine / Ignition / Fuel",
        "possible_causes": [
            "Spark plug problem",
            "Ignition coil problem",
            "Fuel injector problem",
            "Air/fuel mixture problem",
            "Compression or mechanical problem"
        ]
    },

    "P0302": {
        "description": "Cylinder 2 misfire detected",
        "system": "Engine / Ignition / Fuel",
        "possible_causes": [
            "Spark plug problem",
            "Ignition coil problem",
            "Fuel injector problem",
            "Air/fuel mixture problem",
            "Compression or mechanical problem"
        ]
    },

    "P0303": {
        "description": "Cylinder 3 misfire detected",
        "system": "Engine / Ignition / Fuel",
        "possible_causes": [
            "Spark plug problem",
            "Ignition coil problem",
            "Fuel injector problem",
            "Air/fuel mixture problem",
            "Compression or mechanical problem"
        ]
    },

    "P0304": {
        "description": "Cylinder 4 misfire detected",
        "system": "Engine / Ignition / Fuel",
        "possible_causes": [
            "Spark plug problem",
            "Ignition coil problem",
            "Fuel injector problem",
            "Air/fuel mixture problem",
            "Compression or mechanical problem"
        ]
    },

    "P0171": {
        "description": "System too lean",
        "system": "Fuel / Air Intake",
        "possible_causes": [
            "Vacuum leak",
            "Air intake leak",
            "Fuel delivery problem",
            "Injector issue",
            "Sensor-related problem"
        ]
    },

    "P0172": {
        "description": "System too rich",
        "system": "Fuel / Air Intake",
        "possible_causes": [
            "Excess fuel delivery",
            "Air intake measurement problem",
            "Injector issue",
            "Sensor-related problem"
        ]
    },

    "P0420": {
        "description": "Catalyst system efficiency below threshold",
        "system": "Exhaust / Emissions",
        "possible_causes": [
            "Catalytic converter efficiency problem",
            "Exhaust leak",
            "Oxygen sensor issue",
            "Engine running condition affecting catalyst performance"
        ]
    },

    "P0128": {
        "description": "Coolant thermostat temperature below regulating temperature",
        "system": "Cooling System",
        "possible_causes": [
            "Thermostat problem",
            "Coolant temperature sensor issue",
            "Cooling-system related problem"
        ]
    },

    "P0562": {
        "description": "System voltage low",
        "system": "Electrical / Charging",
        "possible_causes": [
            "Weak battery",
            "Charging-system problem",
            "Alternator issue",
            "Electrical connection problem"
        ]
    }
}
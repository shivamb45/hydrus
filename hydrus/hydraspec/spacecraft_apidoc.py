spacecraft_apidoc = {
    "@type": "ApiDocumentation",
    "title": "The name of the API",
    "supportedClass": [
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                }
            ],
            "title": "cubicMillimeters",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "label": "Creates a new cubicMillimeters entity",
                    "method": "POST",
                    "@id": "_:cubicMillimeters_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the cubicMillimeters entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "label": "Replaces an existing cubicMillimeters entity",
                    "method": "PUT",
                    "@id": "_:cubicMillimeters_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a cubicMillimeters entity",
                    "method": "DELETE",
                    "@id": "_:cubicMillimeters_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the cubicMillimeters entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "label": "Retrieves a cubicMillimeters entity",
                    "method": "GET",
                    "@id": "_:cubicMillimeters_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "unit of measure for volume",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/objective",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/isComponentOf",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVoltage",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_Detector",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "label": "Creates a new Spacecraft_Detector entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_Detector_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Detector entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "label": "Replaces an existing Spacecraft_Detector entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_Detector_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_Detector entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_Detector_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Detector entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "label": "Retrieves a Spacecraft_Detector entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_Detector_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "A space detector is a sensor supported by another device that let it collect data, that is deployed into a spacecraft and works outside Earth lower atmosphere",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/typeOfPropellant",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_Propulsion.",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "label": "Creates a new Spacecraft_Propulsion. entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_Propulsion._create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Propulsion. entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "label": "Replaces an existing Spacecraft_Propulsion. entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_Propulsion._replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_Propulsion. entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_Propulsion._delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Propulsion. entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "label": "Retrieves a Spacecraft_Propulsion. entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_Propulsion._retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Complex devices-subsystems used for impelling (processes of applying a force which results in translational motion) a spacecraft, in the specific http://umbel.org/umbel/rc/ProjectilePropelling",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasEfficiency",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVoltage",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_PrimaryPower.",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "label": "Creates a new Spacecraft_PrimaryPower. entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_PrimaryPower._create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_PrimaryPower. entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "label": "Replaces an existing Spacecraft_PrimaryPower. entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_PrimaryPower._replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_PrimaryPower. entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_PrimaryPower._delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_PrimaryPower. entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "label": "Retrieves a Spacecraft_PrimaryPower. entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_PrimaryPower._retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Complex devices-subsystems used for collecting energy.",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_BackupPower",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "label": "Creates a new Spacecraft_BackupPower entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_BackupPower_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_BackupPower entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "label": "Replaces an existing Spacecraft_BackupPower entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_BackupPower_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_BackupPower entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_BackupPower_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_BackupPower entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "label": "Retrieves a Spacecraft_BackupPower entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_BackupPower_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Complex devices-subsystems used for storing energy.",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_Thermal",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "label": "Creates a new Spacecraft_Thermal entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_Thermal_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "label": "Replaces an existing Spacecraft_Thermal entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_Thermal_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_Thermal entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_Thermal_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "label": "Retrieves a Spacecraft_Thermal entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_Thermal_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Shields, shells or any device insulation from/reflecting radiation exploiting emission and absorption events",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_Thermal_PassiveDevice",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "label": "Creates a new Spacecraft_Thermal_PassiveDevice entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_PassiveDevice entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "label": "Replaces an existing Spacecraft_Thermal_PassiveDevice entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_Thermal_PassiveDevice entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_PassiveDevice entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "label": "Retrieves a Spacecraft_Thermal_PassiveDevice entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "They are passive because they mostly transform radiation into heating/cooling ",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_Thermal_ActiveDevice",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "label": "Creates a new Spacecraft_Thermal_ActiveDevice entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_ActiveDevice entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "label": "Replaces an existing Spacecraft_Thermal_ActiveDevice entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_Thermal_ActiveDevice entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_ActiveDevice entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "label": "Retrieves a Spacecraft_Thermal_ActiveDevice entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Complex devices-subsystems used to protect sensors or electronic devices from over/under-heating, like refrigeration absorption.",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/standsMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_Structure",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "label": "Creates a new Spacecraft_Structure entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_Structure_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Structure entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "label": "Replaces an existing Spacecraft_Structure entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_Structure_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_Structure entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_Structure_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Structure entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "label": "Retrieves a Spacecraft_Structure entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_Structure_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "It's the skeleton and framework of the spacecraft.",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVoltage",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxClock",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinClock",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasDataStorage",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasDataStorageExternal",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasRAM",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_CDH",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "label": "Creates a new Spacecraft_CDH entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_CDH_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_CDH entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "label": "Replaces an existing Spacecraft_CDH entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_CDH_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_CDH entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_CDH_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_CDH entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "label": "Retrieves a Spacecraft_CDH entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_CDH_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "The DH system shall: Enable HK and science data flow \u2013 Housekeeping data (Temperatures, Pressures, Voltages, Currents, Status,...) \u2013 Attitude data \u2013 Payload data (e.g., Science data) - Receive and distribute commands - Perform TM and TC protocols - Distribute timing signals - Synchronization of data \u2013 Time stamping of data - Provide data storage - Execute commands and schedules - Control subsystems and payloads - Monitor spacecraft health - Make autonomous decisions - Perform data compression.",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_Communication",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "label": "Creates a new Spacecraft_Communication entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_Communication_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Communication entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "label": "Replaces an existing Spacecraft_Communication entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_Communication_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_Communication entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_Communication_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Communication entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "label": "Retrieves a Spacecraft_Communication entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_Communication_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Complex devices-subsystems used for transmitting/receiving radio waves.",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "embedSensor",
                    "property": "http://ontology.projectchronos.eu/subsystems/embedSensor",
                    "description": "a subsystem that holds a sensor",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/standsMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_AODCS",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "label": "Creates a new Spacecraft_AODCS entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_AODCS_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "label": "Replaces an existing Spacecraft_AODCS entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_AODCS_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_AODCS entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_AODCS_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "label": "Retrieves a Spacecraft_AODCS entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_AODCS_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Complex devices-subsystems used to set the direction and the position of the spacecraft, it controls flight dynamics.",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_AODCS_Active",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "label": "Creates a new Spacecraft_AODCS_Active entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_AODCS_Active_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_Active entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "label": "Replaces an existing Spacecraft_AODCS_Active entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_AODCS_Active_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_AODCS_Active entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_AODCS_Active_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_Active entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "label": "Retrieves a Spacecraft_AODCS_Active entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_AODCS_Active_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "Do NOT use any additional power from the spacecraft generator",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice"
        },
        {
            "@type": "Class",
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "title": "isSubsystemOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "description": "subject is a device or a system of devices that is subsystem of a wider system or device",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isComponentOf",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isComponentOf",
                    "description": "the subject is a member of a wider artifact, that is a set of artifacts",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "hasSubSystem",
                    "property": "http://ontology.projectchronos.eu/spacecraft/hasSubSystem",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "title": "isDeployedIn",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isDeployedIn",
                    "description": "the environment in which a device or a system of devices is designed to work",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false"
                },
                {
                    "required": "false",
                    "@type": "SupportedProperty",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false"
                }
            ],
            "title": "Spacecraft_AODCS_PassiveDevice",
            "supportedOperation": [
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "label": "Creates a new Spacecraft_AODCS_PassiveDevice entity",
                    "method": "POST",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_create",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_PassiveDevice entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "label": "Replaces an existing Spacecraft_AODCS_PassiveDevice entity",
                    "method": "PUT",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_replace",
                    "description": "null",
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice"
                },
                {
                    "statusCodes": [],
                    "@type": "hydraspec:Operation",
                    "returns": "null",
                    "label": "Deletes a Spacecraft_AODCS_PassiveDevice entity",
                    "method": "DELETE",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_delete",
                    "description": "null",
                    "expects": "null"
                },
                {
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_PassiveDevice entity wasn't found."
                        }
                    ],
                    "@type": "hydraspec:Operation",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "label": "Retrieves a Spacecraft_AODCS_PassiveDevice entity",
                    "method": "GET",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_retrieve",
                    "description": "null",
                    "expects": "null"
                }
            ],
            "description": "DO use any additional power from the spacecraft generator",
            "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice"
        }
    ],
    "possibleStatus": [],
    "description": "A short description of the API",
    "@context": "http://www.w3.org/ns/hydraspec/context.jsonld",
    "@id": "http://api.example.com/doc/",
    "entrypoint": "URL of the API's main entry point"
}
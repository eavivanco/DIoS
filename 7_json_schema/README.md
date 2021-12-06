# JSONSchema

References : 

[Street Lighting](https://github.com/smart-data-models/dataModel.Streetlighting)

Here you will find :

1. JSONSchema for Streetlight in ```SLschema.json ```
   
   1. Code implemented : 

```"lampColor": {
    "type": "string",
    "description": "Property. Lamp's light color. Model:'https://schema.org/color'. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)"
    },
```
   2. API augmentation : ```lampColor``` : The color of the lamp of this Streetlight. 


2. JSNOSchema for StreetlightControlCabinet in ```SLCCschema.json ```

   1.  Code implemented :

```"lampColor": {
    "type": "string",
    "description": "Property. Lamp's light color controled by this cabinet. Model:'https://schema.org/color'. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)"
    },
```
   2. API augmentation :  ```lampColor``` : The color of the lamp of the Streetlight individual or group controled by this cabinet.


3. JSONSchema for StreetlightGroup in ```SLGschema.json ```

   1. Code implemented : 

```"lampColor": {
    "type": "string",
    "description": "Property. Relative lamp's light color setting for the group. Model:'https://schema.org/color'. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)"
    },
```
   2. API augmentation : ```lampColor``` : The color of the lamps of the Streetlights of this group.


4. JSONSchema for StreetlightModel in ```SLMschema.json ```

   1. Code implemented : 

```"lampColor": {
    "type": "string",
    "description": "Property. Lamp's light color. Model:'https://schema.org/color'. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)"
    },
```
   2. API augmentation :  ```lampColor``` : The color of the lamp of this Streetlight.
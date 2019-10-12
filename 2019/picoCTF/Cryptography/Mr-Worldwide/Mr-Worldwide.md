# Mr-Worldwide
## Points: 200 - (Solves: 2899)
### Solved by: Vermillion

### Description

`A musician left us a `[message](message.txt)`. What's it mean?`

Opening up the text file, we see the following line:

`picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}`

It looks like each letter is encoded into a pair of numbers. This pair of numbers immediately stood out to me as latitude and longitude, so perhaps the letters are encoded using the address of the location. The process of finding an address from latitude and longitude is called "Reverse Geocoding". Google Maps has a [good Reverse Geocoding site](https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/geocoding-reverse).

Putting in each of the coordinates gives us the following list of places:

```
Kyoto, Japan
Odessa, Ukraine
Dayton, Ohio, USA
Istanbul, Turkey
Abu Dhabi, UAE
Kuala Lumpur, Malaysia
Addis Ababa, Ethiopia
Loja, Ecuador
Amsterdam, Netherlands
Sleepy Hollow, NY, USA
Kodiak, Alaska, USA
Alexandria, Egypt
```
Combining the first letters of each city gives us `KODIAKALASKA`. Seeing how this was one of the places, this makes sense as a flag. Putting the letters back into the flag gives us the flag:

### Flag:
`picoCTF{KODIAK_ALASKA}`

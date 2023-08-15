// access token is passed from the view to the template 
mapboxgl.accessToken = document.getElementById('map').getAttribute('data-mapbox-access-token');

// get variables from template
var restaurantAddress = document.getElementById('map').getAttribute('data-restaurant-address');
var restaurantName = document.getElementById('map').getAttribute('data-restaurant-name');
var restaurantDescription = document.getElementById('map').getAttribute('data-restaurant-description');
var faviconUrl = document.getElementById('map').getAttribute('data-favicon-url');


// Create custompin
var customPin = document.createElement('div');
customPin.className = 'custom-marker';
customPin.style.backgroundImage = `url("${faviconUrl}")`;



fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/${restaurantAddress}.json?access_token=${mapboxgl.accessToken}`)
  .then(response => response.json())
  .then(data => {
    var coordinates = data.features[0].center;

    var map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v12',
      center: coordinates,
      zoom: 14,
    });

    var geojson = {
      type: 'Feature',
      geometry: {
        type: 'Point',
        coordinates: coordinates
      },
      properties: {
        title: restaurantName,
        description: restaurantDescription
      }
    };

    // Create a new marker and set popup
    new mapboxgl.Marker(customPin)
    .setLngLat(coordinates)
    .setPopup(new mapboxgl.Popup().setHTML('<h3>' + geojson.properties.title + '</h3><p>' + geojson.properties.description + '</p>')) // Customize the popup content
    .addTo(map);
  });

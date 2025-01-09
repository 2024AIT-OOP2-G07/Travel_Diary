async function getRestaurantFeatures() {
  const points = await fetch("/api/points")
    .then((res) => res.json())
    .catch((err) => {
      console.error(err);
      return [];
    });
  const features = [];
  points.map((point) =>
    features.push({
      type: "Feature",
      properties: {
        day: point.day,
        name: point.name,
        address: point.address,
        evaluation: point.evaluation,
        comment: point.comment,
      },
      geometry: {
        type: "Point",
        coordinates: [point.lon, point.lat],
      },
    })
  );
  return features;
}

let features = [];
getRestaurantFeatures().then((res) => {
  features = res;
});

const map = new maplibregl.Map({
  container: "map",
  center: [136.8866387, 35.1723783],
  maxPitch: 85,
  zoom: 14,
  style: {
    version: 8,
    sources: {
      "background-osm-raster": {
        type: "raster",
        tiles: ["https://tile.openstreetmap.jp/styles/osm-bright-ja/{z}/{x}/{y}.png"],
        tileSize: 256,
        attribution:
          "<a href='https://www.openstreetmap.org/copyright' target='_blank'>© OpenStreetMap contributors</a>",
      },
    },
    layers: [
      {
        id: "background-osm-raster",
        type: "raster",
        source: "background-osm-raster",
      },
    ],
  },
});

map.on("load", async () => {
  const iconImage = await map.loadImage("../static/star.png");
  map.addImage("trip_point_icon", iconImage.data);
  map.addSource("trip_point", {
    type: "geojson",
    data: {
      type: "FeatureCollection",
      name: "point",
      crs: { type: "name", properties: { name: "urn:ogc:def:crs:OGC:1.3:CRS84" } },
      features: features,
    },
  });
  map.addLayer({
    id: "trip_point",
    type: "symbol",
    source: "trip_point",
    layout: {
      "icon-image": "trip_point_icon",
      "icon-size": 0.5,
    },
  });
});

map.on("click", "trip_point", (e) => {
  const coordinates = e.features[0].geometry.coordinates.slice();
  const message = `
    <strong>${e.features[0].properties.name}</strong>
    <p>${e.features[0].properties.address}</p>
    <p>評価: ${e.features[0].properties.evaluation}</p>
    <p>${e.features[0].properties.comment}</p>
    <a href="/points#${e.features[0].properties.name}">詳細を見る</a>
    `;

  while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
    coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
  }
  new maplibregl.Popup({
    offset: 10,
    closeButton: false,
  })
    .setLngLat(coordinates)
    .setHTML(message)
    .addTo(map);
});

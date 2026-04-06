export default function PropertyCard({ property, buy }) {
  return (
    <div className="card">
      <h3>{property.name}</h3>
      <p>{property.location}</p>
      <p>₹{property.price}</p>
      <button onClick={() => buy(property.id)}>Buy Share</button>
    </div>
  );
}
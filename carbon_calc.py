import streamlit as st

def estimate_carbon_footprint(text_queries, image_generations, video_minutes, region='Global'):
    """
    Estimate carbon footprint based on AI inference usage.
    """
    # Energy usage per query (Wh) - approximate values
    text_query_energy = 2.9  # Wh per ChatGPT query
    image_gen_energy = 2.5   # Wh per image generation
    video_gen_energy = 100   # Wh per minute of AI-generated video
    
    # Convert to total energy use (Wh)
    total_energy = (
        (text_queries * text_query_energy) + 
        (image_generations * image_gen_energy) + 
        (video_minutes * video_gen_energy)
    )
    
    # Carbon intensity (g CO₂ per kWh) by region
    carbon_intensity = {
        'Global': 400,
        'US': 370,
        'EU': 250,
        'China': 500,
        'India': 600
    }
    
    # Convert Wh to kWh, then multiply by carbon intensity
    carbon_footprint = (total_energy / 1000) * carbon_intensity.get(region, 400)
    
    return carbon_footprint

def main():
    st.title("AI Carbon Footprint Calculator")
    st.write("Estimate the carbon footprint of your AI usage based on inference activity.")
    
    # User input
    text_queries = st.number_input("Number of AI text queries per day", min_value=0, value=10)
    image_generations = st.number_input("Number of AI-generated images per day", min_value=0, value=5)
    video_minutes = st.number_input("Minutes of AI-generated video per day", min_value=0, value=2)
    region = st.selectbox("Select your region", ["Global", "US", "EU", "China", "India"])
    
    # Compute footprint
    daily_carbon = estimate_carbon_footprint(text_queries, image_generations, video_minutes, region)
    monthly_carbon = daily_carbon * 30
    yearly_carbon = daily_carbon * 365
    
    # Comparisons
    driving_miles = daily_carbon / 404  # Avg CO₂ per mile driven
    smartphones_charged = daily_carbon / 50  # Avg CO₂ per smartphone charge
    flight_km = daily_carbon / 90  # Approximate CO₂ per km flown
    
    # Display results
    st.subheader("Your AI Carbon Footprint Estimates")
    st.write(f"Daily CO₂ Emissions: {daily_carbon:.2f} g CO₂")
    st.write(f"Monthly CO₂ Emissions: {monthly_carbon:.2f} g CO₂")
    st.write(f"Yearly CO₂ Emissions: {yearly_carbon:.2f} g CO₂")
    
    st.subheader("Real-World Equivalents")
    st.write(f"Daily AI use is equivalent to **driving {driving_miles:.1f} miles.**")
    st.write(f"Or charging your smartphone **{smartphones_charged:.0f} times.**")
    st.write(f"Or flying approximately **{flight_km:.1f} km/{(flight_km*.621):.1f} miles.**")
    
    st.subheader("Inference vs. Training")
    st.write("Over time, inference quickly overtakes training in energy use. ")
    st.write("While training a model like GPT-4 uses massive upfront energy, inference runs 24/7 at scale, making it the bigger long-term driver of AI’s carbon footprint.")
    
    st.write("### Ways to Reduce Your AI Carbon Footprint:")
    st.write("- Use AI efficiently (batch queries, avoid unnecessary generation)")
    st.write("- Choose AI providers that use renewable energy (Google Cloud, Microsoft Azure)")
    st.write("- Consider running AI locally on energy-efficient devices where possible")

    st.write("Created by Jordan Harrod with coding assistance from ChatGPT 4o. Last updated: February 4, 2025")
    
if __name__ == "__main__":
    main()

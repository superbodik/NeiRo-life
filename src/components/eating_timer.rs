use bevy::ecs::system::Resource;
use bevy::time::Timer;

pub struct FoodSpawnTimer(pub Timer);

impl Resource for FoodSpawnTimer {}

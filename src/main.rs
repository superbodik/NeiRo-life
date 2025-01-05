mod game;
mod components;
mod systems;
mod utils;
mod config;
use crate::components::eating_timer::FoodSpawnTimer;
use crate::systems::interaction::{setup_creature, spawn_food_system};
use std::time::Duration;

use bevy::prelude::*;
use bevy::prelude::App;

fn main() {
    App::new()
        .add_plugins(DefaultPlugins)
        .insert_resource(FoodSpawnTimer(Timer::new(Duration::from_secs(5), TimerMode::Repeating)))
        .add_startup_system(setup_creature)
        .add_system(spawn_food_system)
        .run();
}
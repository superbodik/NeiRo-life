use bevy::prelude::*;

#[derive(Component)]
pub struct Creature {
    pub health: f32,
    pub speed: f32,
}

impl Default for Creature {
    fn default() -> Self {
        Creature { health: 100.0, speed: 2.0 }
    }
}

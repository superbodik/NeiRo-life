use bevy::prelude::*;

#[derive(Component)]
pub struct Food {
    pub energy: f32,
}

impl Default for Food {
    fn default() -> Self {
        Food { energy: 20.0 } 
    }
}

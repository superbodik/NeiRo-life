use bevy::prelude::*;
use crate::components::{creature::Creature, food::Food};

pub fn setup_world(mut commands: Commands) {

    commands.spawn(Camera2dBundle::default());

    for i in 0..5 {
        commands.spawn((
            Creature { health: 100.0, speed: 2.0 },
            Transform {
                translation: Vec3::new(i as f32 * 100.0, 0.0, 0.0),
                ..Default::default()
            },
            GlobalTransform::default(),
        ));
    }

    for i in 0..5 {
        commands.spawn((
            Food { energy: 20.0 },
            Transform {
                translation: Vec3::new(i as f32 * 120.0 + 50.0, 0.0, 0.0),
                ..Default::default()
            },
            GlobalTransform::default(),
        ));
    }
}

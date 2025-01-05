use bevy::prelude::*;
use crate::components::{creature::Creature, food::Food};
use crate::components::eating_timer::FoodSpawnTimer;
use rand::Rng;
use std::time::Duration;

pub fn spawn_food_system(
    mut commands: Commands,
    time: Res<Time>,
    mut timer: ResMut<FoodSpawnTimer>,
) {
    timer.0.tick(time.delta());

    if timer.0.finished() {
        let mut rng = rand::thread_rng();
        let random_position = Vec3::new(
            rng.gen_range(-500.0..500.0),
            0.0,
            rng.gen_range(-500.0..500.0),
        );

        // Используем spawn и передаем компоненты напрямую
        commands.spawn((
            Food { energy: 20.0 },
            Transform::from_translation(random_position),
            Sprite {
                color: Color::rgb(1.0, 0.0, 0.0), // Красный цвет
                ..Default::default()
            },
        ));

        timer.0 = Timer::new(Duration::from_secs(rng.gen_range(5..15)), TimerMode::Repeating);
    }
}

pub fn setup_creature(mut commands: Commands) {
    // Используем spawn и передаем компоненты напрямую
    commands.spawn((
        Creature { health: 100.0, speed: 2.0 },
        Transform::from_translation(Vec3::new(0.0, 0.0, 0.0)),
        Sprite {
            color: Color::rgb(0.0, 0.0, 1.0), // Синий цвет
            ..Default::default()
        },
    ));
}

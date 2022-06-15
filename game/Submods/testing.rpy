init -990 python:
    store.mas_submod_utils.Submod(
        author="A",
        name="Test",
        description="Solo Test",
        version="1.0"
    )

# Register the updater
init -990 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Testing",
            user_name="dezlock",
            repository_name="test_submod",
            update_dir=""
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_reload_custom",
            prompt="Custom message?",
            category=['Testing'],
            pool=True,
            unlocked=True,
        ),
        markSeen=False
    )

label monika_reload_custom:
    m 1hub "Alright!"
    play sound "submods/coin_flip_sfx.wav"
    pause 1.0
    m 1hub "Done!"
    return
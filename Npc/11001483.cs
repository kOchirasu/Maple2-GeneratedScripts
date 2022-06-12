using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001483: Mue
/// </summary>
public class _11001483 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0106111607005777$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0106111607005780$
                // - Ooh... This temple creeps me out. I can't find anyone in this gloomy place...
                return 30;
            case (30, 1):
                // $script:0106111607005781$
                // - D-do you see the door over there? I think something awful happened on the other side... I'm scared...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

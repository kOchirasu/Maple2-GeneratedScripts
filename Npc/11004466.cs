using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004466: Richmonde Guard
/// </summary>
public class _11004466 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012101$
    // - All's we—Huh?! You're an outlander!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012102$
                // - All's we—Huh?! You're an outlander!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

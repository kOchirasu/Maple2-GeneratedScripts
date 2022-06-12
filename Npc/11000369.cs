using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000369: NRL-A
/// </summary>
public class _11000369 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407001520$
    // - Beep!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001521$
                // - Beep! Unauthorized access.
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

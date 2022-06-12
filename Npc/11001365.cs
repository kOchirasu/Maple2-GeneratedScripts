using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001365: Dunba
/// </summary>
public class _11001365 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1215222907005048$
    // - Sigh... I'm so glad that everyone's safe.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1230171207005755$
                // - I hope the Blackstars leave me alone this time... I don't want a rematch with Vasara Chen...
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

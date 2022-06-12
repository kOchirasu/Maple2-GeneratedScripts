using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004541: Nuel
/// </summary>
public class _11004541 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0110183907012675$
    // - Ugh... I hate deadlines...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0110183907012676$
                // - Ugh... I hate deadlines...
                return 10;
            case (10, 1):
                // $script:0110183907012677$
                // - Here to gawk at the soldierettos? Get a good look and then be on your way. I can't concentrate with all you... all you tourists hanging about!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

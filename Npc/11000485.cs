using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000485: Mushkid
/// </summary>
public class _11000485 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002129$
    // - What's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002132$
                // - Down below, $npcName:22000321$ has claimed all of the $map:2000202$ for herself!
                return 30;
            case (30, 1):
                // $script:0831180407002133$
                // - She's bad, but... so cool! I want to be a monster mushroom like her!
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

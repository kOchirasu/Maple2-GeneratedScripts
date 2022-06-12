using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004550: Office Guard
/// </summary>
public class _11004550 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0109163907012665$
    // - This is $npcName:11004401[gender:1]$'s office. I don't know what your business is, but you watch yourself around $npcName:11004401[gender:1]$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0109163907012666$
                // - This is $npcName:11004401[gender:1]$'s office. I don't know what your business is, but you watch yourself around $npcName:11004401[gender:1]$.
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

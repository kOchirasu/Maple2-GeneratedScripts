using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000704: Rove
/// </summary>
public class _11000704 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002833$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002834$
                // - Come to sample our juice? $npcName:11000445[gender:1]$ right here will set you up. Hope you're ready for a trip to flavor country!
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

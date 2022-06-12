using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001375: Bolden
/// </summary>
public class _11001375 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005356$
    // - Wah! You startled me!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005359$
                // - Welcome! L-look, just ignore them and keep your eyes on me, okay? Eheheh...
                return 30;
            case (30, 1):
                // $script:1217144507005360$
                // - Eager to get out of here? Try the latest model sports car from Tuning Motors. Just start the engine and leave this dump in the dust!
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

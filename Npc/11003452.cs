using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003452: Brave Pig
/// </summary>
public class _11003452 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008659$
    // - It's a family name.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008660$
                // - You didn't think I'd actually be a pig, did you?
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

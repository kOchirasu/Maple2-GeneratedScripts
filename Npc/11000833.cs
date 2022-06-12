using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000833: Alponi
/// </summary>
public class _11000833 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003047$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003050$
                // - Ooh, I hate wolves more than anything. They chew up our fences and take our sheep. I wish I could just move away... me and the sheep... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

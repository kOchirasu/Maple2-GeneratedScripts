using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003448: Tina
/// </summary>
public class _11003448 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008651$
    // - The people need a reason to raise their heads up high.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008652$
                // - We're all in this together.
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

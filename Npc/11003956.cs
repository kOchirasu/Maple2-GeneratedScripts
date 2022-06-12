using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003956: Priest
/// </summary>
public class _11003956 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010003$
    // - Do you believe in the power of the light?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010004$
                // - This Frontier Foundation is a beautiful place. I look forward to working with such capable individuals.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

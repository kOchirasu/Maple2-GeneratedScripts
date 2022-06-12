using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000216: Humphrey
/// </summary>
public class _11000216 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000944$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000946$
                // - Money, money, money! That's always the problem. $npcName:11000252[gender:0]$ is obsessed with money, and $npcName:11000065[gender:0]$ only cares about development. If they really got together to fool the citizens, we'll make them pay for it!
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

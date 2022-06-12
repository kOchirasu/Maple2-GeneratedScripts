using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000058: Elmin
/// </summary>
public class _11000058 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407000255$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000258$
                // - If I had stayed with Bella that day... 
                return -1;
            case (40, 0):
                // $script:0831180407000259$
                // - I used to live here with my family, but... I'm the only one living in this house now. I miss them so much...
                return -1;
            case (50, 0):
                // $script:0831180407000260$
                // - Sometimes I sit by the window, watching the stars fade away one by one, reminiscing about the good old days. I try not to recall the sad memories, but only the good, happy ones.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

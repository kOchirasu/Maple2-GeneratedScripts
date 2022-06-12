using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001410: Dona
/// </summary>
public class _11001410 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217205907005407$
    // - You came to gawk at the Meerkat Patrols? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1222203907005494$
                // - We all trust and rely on each other in the Meerkat Patrol. You could say we're a big happy family.
                switch (selection) {
                    // $script:1222203907005495$
                    // - What's the secret to your camaraderie?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1222203907005496$
                // - It's all thanks to our hardworking captain. We all look up to good old Captain $npcName:11001408[gender:0]$! 
                return 41;
            case (41, 1):
                // $script:1222203907005497$
                // - Since you're here, you should say hi to him. I bet he'll have some good advice for you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001706: Tinchai
/// </summary>
public class _11001706 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006958$
    // - Mm? Yes?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507006980$
                // - It's good to see you, $MyPCName$. Is there something I can get for you?
                switch (selection) {
                    // $script:0804030507007003$
                    // - What is this artifact we're after?
                    case 0:
                        return 40;
                    // $script:0804030507007004$
                    // - Should we be looking for the master?
                    case 1:
                        return 50;
                }
                return -1;
            case (40, 0):
                // $script:0804030507007005$
                // - I don't know exactly what it is, but supposedly Lone Spirit, the founder of Guidance, left behind a treasure that would grant enlightenment to his true heir. It was passed down through generations... until the eleventh Munakra vanished with it.
                return 40;
            case (40, 1):
                // $script:0804030507007006$
                // - Some people think it was destroyed. Others think that all of its power was drained, and it's been placed in hiding until it can recharge. Others say that Lone Spirit reincarnated and claimed it for himself. Who knows which theory, if any, is true?
                return 40;
            case (40, 2):
                // $script:0804030507007007$
                // - The only reliable information on the artifact is told through word-of-mouth, so the only one who would really know is the master. What if... what if $npcName:11001559[gender:0]$ came to Halo Mountain for the artifact?
                return 40;
            case (40, 3):
                // $script:0804030507007008$
                // - That must be it. I'm sure he said something about an artifact when he attacked us...
                //   <font color="#909090">($npcName:11001706[gender:1]$ is lost in thought.)</font>
                switch (selection) {
                    // $script:0804030507007009$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (50, 0):
                // $script:0804030507007010$
                // - The master can fend for himself. Don't worry, all right?
                //   <font color="#909090">(Even as she comforts you, worry is etched in her face.)</font>
                switch (selection) {
                    // $script:0804030507007011$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}

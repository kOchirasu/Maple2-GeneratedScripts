using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001557: Junta
/// </summary>
public class _11001557 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0617105607006361$
    // - Have you been training? Answer carefully.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006796$
                // - Get to the point.
                switch (selection) {
                    // $script:0727223007006797$
                    // - I want to know the secrets of animus.
                    case 0:
                        return 40;
                    // $script:0727223007006798$
                    // - Tell me about last year's incident.
                    case 1:
                        return 50;
                    // $script:0727223007006799$
                    // - Why aren't there more students of Guidance?
                    case 2:
                        return 60;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006800$
                // - Knowledge is just as important as strength. For that reason, I will answer your questions, no matter how stupid they are. Don't make me repeat myself.
                return 40;
            case (40, 1):
                // $script:0727223007006801$
                // - Animus is both the core philosophy and the energy developed by the Lone Spirit, who founded our order long ago. When you become one with nature, you can harness this energy and turn it into martial power.
                return 40;
            case (40, 2):
                // $script:0727223007006802$
                // - The outsiders wield a similar force that they call magic. Animus is more powerful, of course, but it takes years of dedicated training to master.
                //   <font color="#909090">(He eyes you coolly.)</font>
                switch (selection) {
                    // $script:0727233607006912$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (50, 0):
                // $script:0727223007006803$
                // - The master and I were traveling the Land of Darkness on a training journey when we heard a series of explosions. We followed the sound and found you, dying.
                return 50;
            case (50, 1):
                // $script:0727233607006913$
                // - I didn't even realize you were alive at first, you were so close to death. The master tried to cure you, but you were too far gone.
                return 50;
            case (50, 2):
                // $script:0727223007006804$
                // - The master refused to let you die. He channeled his animus into you so that you would live. Do you understand what that means?
                switch (selection) {
                    // $script:0727223007006805$
                    // - No.
                    case 0:
                        return 51;
                    // $script:0727223007006806$
                    // - Yes.
                    case 1:
                        return 52;
                }
                return -1;
            case (51, 0):
                // $script:0727223007006807$
                // - If you don't understand your roots, you will never know wisdom. If you don't show gratitude, you will never know humanity. And you... You know neither. So just listen and nod.
                return 51;
            case (51, 1):
                // $script:0727223007006808$
                // - I begged him not to, but he gave you a portion of his power. He didn't simply heal you... he transferred his animus into you. Animus developed over centuries of training.
                return 51;
            case (51, 2):
                // $script:0727223007006809$
                // - I don't understand why the master was so determined to save you, but your life is his now. The only way to repay him is to train as hard as you can and become a great student of Guidance.
                switch (selection) {
                    // $script:0727233607006914$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (52, 0):
                // $script:0727223007006810$
                // - If you knew that, maybe you wouldn't have slacked off in your training so much! Did you really think I wouldn't notice? You need to put your all into it!
                switch (selection) {
                    // $script:0727233607006915$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (60, 0):
                // $script:0727223007006811$
                // - There is only you, myself, and $npcName:11001699[gender:1]$. Does it bother you that there are only three of us?
                return 60;
            case (60, 1):
                // $script:0727223007006812$
                // - When I joined Guidance, there were quite a few students. In its heyday, the mountain was teeming with them.
                switch (selection) {
                    // $script:0727223007006813$
                    // - Where did they all go?
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:0727223007006814$
                // - They left for various reasons. Some thought the training was too hard. Others left to join the world of humans after their training journey. A few only wanted to learn some simple tricks, and left as soon as they'd done so.
                return 61;
            case (61, 1):
                // $script:0727223007006815$
                // - A few of our former students created their own group in the outside world. If they couldn't make it here, I doubt they'd have much success on their own. They certainly wouldn't hold to our values of integrity and righteousness...
                return 61;
            case (61, 2):
                // $script:0727223007006816$
                // - What did they call themselves? The Blackwinds? The Jaw Smashers? Something insane like that. Let their mistakes be a reminder to stay on the path of training.
                switch (selection) {
                    // $script:0727233607006916$
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
            (40, 2) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.Next,
            (51, 2) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Next,
            (61, 1) => NpcTalkButton.Next,
            (61, 2) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}

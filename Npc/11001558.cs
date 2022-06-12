using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001558: Tinchai
/// </summary>
public class _11001558 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0617105607006362$
    // - Mm? Yes?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006819$
                // - What do you need? Maybe I can help.
                switch (selection) {
                    // $script:0727223007006820$
                    // - I had a strange dream...
                    case 0:
                        return 40;
                    // $script:0727223007006821$
                    // - I want to know more about Guidance.
                    case 1:
                        return 50;
                    // $script:0727223007006822$
                    // - How long was I out?
                    case 2:
                        return 60;
                    // $script:0727223007006823$
                    // - Tell me about the master.
                    case 3:
                        return 70;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006824$
                // - That would explain all the mumbling. It wasn't... <i>the</i> dream, was it?
                switch (selection) {
                    // $script:0727223007006825$
                    // - No... It was different this time...
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0727223007006826$
                // - That's a relief! I think I'd go crazy if I kept having nightmares about being chased by some mysterious figure.
                switch (selection) {
                    // $script:0727223007006827$
                    // - I dreamed about the first time I met the master and $npcName:11001557[gender:0]$.
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0727223007006828$
                // - That's the earliest memory you have, isn't it? It must have made a real impression! And why not? The first time I met you also left an impression.
                switch (selection) {
                    // $script:0727223007006829$
                    // - Not a bad impression, I hope!
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:0727223007006830$
                // - No, no, not bad, just... startling. The members of Guidance have always been animal folk, at least until you came along. I never expected to see the master and $npcName:11001557[gender:0]$ return to Halo Mountain with a bloodied human in tow.
                return 43;
            case (43, 1):
                // $script:0727223007006831$
                // - I was sure the master would boot you back out as soon as you were walking again. Instead, he took you on as his student. $npcName:11001557[gender:0]$ sure wasn't happy about that...
                switch (selection) {
                    // $script:0727233607006917$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (50, 0):
                // $script:0727223007006832$
                // - For thousands of years, Guidance only ever accepted animal folk into its fold. It was specifically founded by the great Lone Spirit to help us reach enlightenment.
                return 50;
            case (50, 1):
                // $script:0727223007006833$
                // - But that was long ago, and the Lone Spirit's philosophy has surely evolved over millenia of teaching and study. Besides, Halo Mountain is practically empty now, so I say it's time we started accepting more members... including humans like you.
                return 50;
            case (50, 2):
                // $script:0727223007006834$
                // - Before you came along, it was just the master, $npcName:11001557[gender:0]$, and me. But with you, we're now a happy family of four.
                switch (selection) {
                    // $script:0727223007006835$
                    // - Where did all the students go?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0727223007006836$
                // - Some finished their training and left with the master's blessing. Some left to live with the humans. But most of them couldn't handle the training and gave up.
                return 51;
            case (51, 1):
                // $script:0727223007006837$
                // - Regardless of the reasons, we still consider all of them members of Guidance. Well, almost all of them. Some of them started their own group devoted to money and power, not enlightenment. We're not on good terms.
                switch (selection) {
                    // $script:0727233607006918$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (60, 0):
                // $script:0727223007006838$
                // - Half a day, maybe? $npcName:11001557[gender:0]$ was pretty moody about it, since it's the second time you've fainted on us. He just needs to have more patience with your human stamina, if you ask me.
                return 60;
            case (60, 1):
                // $script:0727223007006839$
                // - I don't mind. Taking care of you gives me the chance to relax here and do my antlers. These fairy sparkles take time to get right, y'know. Hey, you want me to do yours? We've got time... if you leave now, then we <i>both</i> have to get back to training...
                switch (selection) {
                    // $script:0727223007006840$
                    // - I'm ready.
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:0727223007006841$
                // - Oh, all right. Guess I can't sit around here <i>all</i> day.
                switch (selection) {
                    // $script:0727223007006842$
                    // - Why do you think I fainted?
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:0727223007006843$
                // - It must be the animus that the master breathed into you. I've never heard of a human using animus before you, so it makes sense it would be hard on your squishy, furless body. Besides, the master's animus is potent even for us animal folk.
                return 62;
            case (62, 1):
                // $script:0727223007006844$
                // - You have a great power inside you, but you're not strong enough to control it. I imagine that feels pretty rough now and then.
                switch (selection) {
                    // $script:0727223007006845$
                    // - I want to know the secrets of animus.
                    case 0:
                        return 63;
                }
                return -1;
            case (63, 0):
                // $script:0727223007006846$
                // - There's nothing secret about it, really. All you have to do is reach unity with nature by disciplining your mind and body, and then harness the energy that creates. The trick is actually <i>doing</i> any of that.
                return 63;
            case (63, 1):
                // $script:0727223007006847$
                // - I'm sure $npcName:11001557[gender:0]$ would be happy to tell you all about it during training.
                switch (selection) {
                    // $script:0727233607006919$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (70, 0):
                // $script:0727223007006848$
                // - Master $npcName:11001556[gender:0]$ is our teacher and the leader of Guidance. He is the fifteenth master to hold the title of Munakra, which means "seeker of knowledge."
                switch (selection) {
                    // $script:0727223007006849$
                    // - Munakra?
                    case 0:
                        return 71;
                }
                return -1;
            case (71, 0):
                // $script:0727223007006850$
                // - The Lone Spirit led Guidance for hundreds of years before he vanished. When the time came, he chose the wisest of his students and bestowed upon them the title of Munakra.
                return 71;
            case (71, 1):
                // $script:0727223007006851$
                // - Since then, the wisest student of each generation receives the title and becomes Guidance's new leader. Our master is the fifteenth in that line. And even if we're pretty small now, we still stand thanks to his leadership. 
                return 71;
            case (71, 2):
                // $script:0727223007006852$
                // - The master makes a yearly pilgrimage to the outside world to help the needy and fight evil. He does it all in secret, too. I think he's done more to help Maple World than any of the Munakra who led Guidance before him.
                switch (selection) {
                    // $script:0727233607006920$
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
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Next,
            (43, 1) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.Next,
            (62, 1) => NpcTalkButton.SelectableDistractor,
            (63, 0) => NpcTalkButton.Next,
            (63, 1) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (71, 0) => NpcTalkButton.Next,
            (71, 1) => NpcTalkButton.Next,
            (71, 2) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}

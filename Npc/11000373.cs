using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000373: Denver
/// </summary>
public class _11000373 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001530$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001532$
                // - I saw you watching me earlier. You're barking up the wrong tree.
                return 20;
            case (20, 1):
                // $script:0831180407001533$
                // - Don't you believe me? I have nothing to hide. Have you always been this nosey?
                return -1;
            case (30, 0):
                // $script:1215105107009707$
                // - Today's such a beautiful day! Wouldn't you agree, friend?
                switch (selection) {
                    // $script:1215105107009708$
                    // - Um, "friend?"
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1215105107009709$
                // - We made eye contact just now, you can't deny it. That makes us pals! Nice to meet you, friend.
                switch (selection) {
                    // $script:1215105107009710$
                    // - Uh, hey buddy. Have you heard the rumors going around?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1215105107009711$
                // - I sure have. Look, I wouldn't go around blabbing this to just anybody, but we're friends, right?
                switch (selection) {
                    // $script:1215105107009712$
                    // - Best friends.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1215105107009713$
                // - So a while back, I was taking a walk. I like going on walks to clear my head. Of course it only works if I go alone. Anyway—
                switch (selection) {
                    // $script:1215105107009714$
                    // - Can you fast-forward to the part where stuff happens?
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1215105107009715$
                // - Right, so I was taking a nice leisurely stroll through Middleton when a giant shadow appeared in the sky!
                return 34;
            case (34, 1):
                // $script:1215105107009716$
                // - I still can't get the image out of my head... giant wings, and these terrible muscly bodies... It was a whole flock of demons! I was terrified.
                switch (selection) {
                    // $script:1215105107009717$
                    // - Wait, then you're the one who started the rumor!
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:1215105107009718$
                // - They're not rumors! It's all true! Would I lie to my best friend?! Besides, I took a picture. Look.
                switch (selection) {
                    // $script:1215105107009719$
                    // - Could I keep this photo? Since we're such good friends.
                    case 0:
                        return 36;
                }
                return -1;
            case (36, 0):
                // $script:1215105107009720$
                // - Sure, if it means you believe me! Take it. I don't know what I'd do if my own friend didn't believe me.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

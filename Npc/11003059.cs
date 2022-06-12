using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003059: Ravole
/// </summary>
public class _11003059 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0102155907007626$
    // - It's nice to meet you!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0102155907007629$
                // - Nice to meet you, $MyPCName$! 
                switch (selection) {
                    // $script:0102155907007630$
                    // - Why did you come here?
                    case 0:
                        return 31;
                    // $script:0102155907007631$
                    // - What does the supply crew do around here?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0102155907007632$
                // - I came here with the supply crew, of course. We're here to keep the guards out here from turning into popsicles. But me... I'm here for another reason.
                switch (selection) {
                    // $script:0102155907007633$
                    // - So, why are you REALLY here?
                    case 0:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0102155907007634$
                // - We keep the guards fed and clothed so they don't freeze or complain too much. Veterans like me handle supplies since we've learned what kind of gear we'll need. Honestly though, there's another reason I'm here.
                switch (selection) {
                    // $script:0102155907007635$
                    // - So, why are you REALLY here?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0102155907007636$
                // - I'm here to study a kingdom that once stood in this snowfield. It was a peaceful kingdom, but no one knows why it vanished into history. The survivors scattered, and none of them will talk to me, so I came here myself.
                return 33;
            case (33, 1):
                // $script:0206154107007917$
                // - I've heard there's a shrine hidden somewhere in the snowfield kingdom. It was meant only for their kings and queens, to hold their most precious treasure. That means if I can get in there, I'll be rich! 
                return 33;
            case (33, 2):
                // $script:0206154107007918$
                // - Hey, this is all completely grounded in fact! That's what my gut tells me, anyway. You look like you can handle a little adventure. If you come across the shrine, you gotta let me know!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.Next,
            (33, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

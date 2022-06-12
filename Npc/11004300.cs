using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004300: Ghost
/// </summary>
public class _11004300 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011395$
    // - What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011398$
                // - I don't gotta answer to you. Now scram, before I get angry.
                switch (selection) {
                    // $script:1002141907011399$
                    // - What brings you here?
                    case 0:
                        return 31;
                    // $script:1002141907011400$
                    // - I'm not here to fight, friend.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011401$
                // - Blackstar goes where the money is! Here's some free advice: keep your nose outta things where it don't belong.
                switch (selection) {
                    // $script:1002141907011402$
                    // - How'd you become a ghost?
                    case 0:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:1002141907011403$
                // - I ain't your friend, pal! You think you can talk down to me 'cause I'm a ghost? Is that it?
                switch (selection) {
                    // $script:1002141907011404$
                    // - How'd you become a ghost?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1002141907011405$
                // - To tell the truth... I got no idea. Boss sent me here on a job, and next thing I know... Pow! Ghost.
                switch (selection) {
                    // $script:1002141907011406$
                    // - There, there. It's okay.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1002141907011407$
                // - I don't want your stinkin' pity! Anyway, this place ain't so bad. It's real cushy, and I got tons of books to read.
                return 34;
            case (34, 1):
                // $script:1002141907011408$
                // - Come to think of it, there were some real important-looking papers in one of the books I read the other day. Weird, huh?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

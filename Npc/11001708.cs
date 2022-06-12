using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001708: Tinchai
/// </summary>
public class _11001708 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006960$
    // - Mm? Yes?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0805021607007079$
                // - I feel... sluggish...
                switch (selection) {
                    // $script:0805021607007080$
                    // - Why's that?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0805021607007081$
                // - Do you know how long it's been since I had a good nap? Ever since we got here, I've been so busy that I haven't had time to train, let alone get my beauty sleep.
                switch (selection) {
                    // $script:0805021607007082$
                    // - Go take a nap now.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0805021607007083$
                // - It wouldn't do any good. I have to get myself good and tired from training, or I can't doze off. So it'll just have to wait!
                //   <font color="#909090">(She gives a cheerful laugh.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000875: Brynner
/// </summary>
public class _11000875 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003181$
    // - I'm going to be rich soon.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003183$
                // - What am I going to do when I become rich? Well... I want a nice-looking house, a nice-looking car, nice-looking clothes, nice-looking shoes... Basically, everything I have should look nice. Right?
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

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000367: Skittle
/// </summary>
public class _11000367 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001514$
    // - What is it, meow?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001516$
                // - Do you believe in love at first sight, meow? I do! Look at the cat next to me. Isn't she beautiful? Me-ow!
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

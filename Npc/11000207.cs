using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000207: Arlano
/// </summary>
public class _11000207 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000889$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000891$
                // - Big cargo ships come through here all the time. Sometimes I think the Barrota Trading Company is more successful than Goldus.
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

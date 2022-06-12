using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000976: Jinbar
/// </summary>
public class _11000976 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003376$
    // - Wa-tcha! Hyoo! <i>That</i> is the sound of a master martial artist!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003378$
                // - Nothing is impossible for true martial artists. Do you want to become strong? It won't be easy. 
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

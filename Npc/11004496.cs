using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004496: Denison
/// </summary>
public class _11004496 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012369$
    // - Ah! You're that $male:fellow,female:lady$, from Sky Fortress. Are you here to ask about my research?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012370$
                // - Ah! You're that $male:fellow,female:lady$, from Sky Fortress. Are you here to ask about my research?
                switch (selection) {
                    // $script:1227192907012371$
                    // - Sure. Tell me about it.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012372$
                // - Since we arrived in Kritias, I've been looking into the connection between the local wildlife and this miraculous "aetherine" substance.
                return 11;
            case (11, 1):
                // $script:1227192907012373$
                // - No matter how big or small, every creature I've sampled has some amount of aetherine in it.
                switch (selection) {
                    // $script:0114164607012726$
                    // - Ah, yes. Fascinating.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114164607012727$
                // - Is there some connection between aetherine and life energy? I'll have to do more science to know for sure.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

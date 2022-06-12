using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001333: Angelina
/// </summary>
public class _11001333 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005252$
    // - Sigh... May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005255$
                // - Judith is usually a good girl, but she can throw a tantrum like nobody's business. All because I refused to buy her a can of her favorite drink...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

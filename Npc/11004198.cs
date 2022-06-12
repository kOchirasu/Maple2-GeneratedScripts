using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004198: Wolf Heart
/// </summary>
public class _11004198 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010644$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010645$
                // - Our yearly pilgrimage through the Vayar Mountains has made the warriors of Murpagoth mighty. Perhaps you will join us on our next journey? That is of course, after we have proven ourselves on the fields of Mushtopia.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

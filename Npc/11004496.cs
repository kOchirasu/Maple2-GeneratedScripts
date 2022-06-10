using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004496: Denison
/// </summary>
public class _11004496 : NpcScript {
    internal _11004496(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012369$ 
                // - Ah! You're that $male:fellow,female:lady$, from Sky Fortress. Are you here to ask about my research? 
                return true;
            case 10:
                // $script:1227192907012370$ 
                // - Ah! You're that $male:fellow,female:lady$, from Sky Fortress. Are you here to ask about my research? 
                switch (selection) {
                    // $script:1227192907012371$
                    // - Sure. Tell me about it.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012372$ 
                // - Since we arrived in Kritias, I've been looking into the connection between the local wildlife and this miraculous "aetherine" substance. 
                // $script:1227192907012373$ 
                // - No matter how big or small, every creature I've sampled has some amount of aetherine in it. 
                switch (selection) {
                    // $script:0114164607012726$
                    // - Ah, yes. Fascinating.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114164607012727$ 
                // - Is there some connection between aetherine and life energy? I'll have to do more science to know for sure. 
                return true;
            default:
                return true;
        }
    }
}

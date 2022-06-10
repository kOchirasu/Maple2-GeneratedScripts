using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003518: Chiumbo
/// </summary>
public class _11003518 : NpcScript {
    internal _11003518(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008854$ 
                // - What is it?
                return true;
            case 30:
                // $script:0817044507008857$ 
                // - What is it?
                switch (selection) {
                    // $script:0817044507008858$
                    // - Tell me about the five auras.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008859$ 
                // - Kiyos live in Zulu Canyon to the northwest. If you capture a kiyo, you can take its Free Spirit.
                switch (selection) {
                    // $script:0817044507008860$
                    // - Tell me about Zulu Canyon.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0817044507008861$
                    // - Tell me about kiyos.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0817044507008862$ 
                // - There are peaks upon peaks at Zulu Canyon. If you don't have wings, you won't be able to cross it.
                switch (selection) {
                    // $script:0817044507008863$
                    // - I need to ask something else.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 33:
                // $script:0817044507008864$ 
                // - The kiyos are agile. They don't like it when anyone gets close.
                switch (selection) {
                    // $script:0817044507008865$
                    // - I need to ask something else.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0817044507008866$ 
                // - W-what?
                switch (selection) {
                    // $script:0817044507008867$
                    // - Tell me about Zulu Canyon.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0817044507008868$
                    // - Tell me about kiyos.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
